import org.apache.spark._
import org.apache.spark.rdd._
import com.amazon.deequ.VerificationSuite
import com.amazon.deequ.checks.{Check, CheckLevel, CheckStatus}
import com.amazon.deequ.constraints.ConstraintStatus

object DeequSparkTest {
    def main(args : Array[String]) : Unit => {
        val sparkConf = new SparkConf()
            .setMaster("local[*]")
            .setAppName("Deequ_Scala")
        val sc = SparkContext(sparkConf)

        case class Item(id: Long, productName: String, description: String, priority: String, numViews: Long)

        val rdd = spark.sparkContext.parallelize(Seq(
            Item(1, "Thingy A", "awesome thing.", "high", 0),
            Item(2, "Thingy B", "available at http://thingb.com", null, 0),
            Item(3, null, null, "low", 5),
            Item(4, "Thingy D", "checkout https://thingd.ca", "low", 10),
            Item(5, "Thingy E", null, "high", 12)))

        val data = spark.createDataFrame(rdd)

        val verificationResult = VerificationSuite()
            .onData(data)
            .addCheck(Check(CheckLevel.Error, "unit testing my data")
                .hasSize(_ == 5) // we expect 5 rows
                .isComplete("id") // should never be NULL
                .isUnique("id") // should not contain duplicates
                .isComplete("productName") // should never be NULL
                .isContainedIn("priority", Array("high", "low")) // should only contain the values "high" and "low"
                .isNonNegative("numViews") // should not contain negative values
                .containsURL("description", _ >= 0.5) // at least half of the descriptions should contain a url
                .hasApproxQuantile("numViews", 0.5, _ <= 10)) // half of the items should have less than 10 views
            .run()
        
        if (verificationResult.status == CheckStatus.Success) {
            println("The data passed the test, everything is fine!")
        } else {
            println("We found errors in the data:\n")
            val resultsForAllConstraints = verificationResult.checkResults.flatMap { case (_, checkResult) => checkResult.constraintResults }
            resultsForAllConstraints.filter { _.status != ConstraintStatus.Success }
                .foreach { result => println(s"${result.constraint}: ${result.message.get}") }
        }
    }
}

