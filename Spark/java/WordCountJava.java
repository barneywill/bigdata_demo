import java.io.*;
import java.util.*;
import java.util.Map.*;

public class WordCountJava {
    public static void main(String[] args) {
        String filePath = args[0];
        BufferedReader reader = null;
        Map<String, Integer> wordCountMap = new HashMap<String, Integer>();
        try {
            reader = new BufferedReader(new InputStreamReader(new FileInputStream(filePath)));
            String line = null;
            while ((line = reader.readLine()) != null) {
                String[] arr = line.split(" ");
                for (String str : arr) {
                    String word = str.replaceAll("[^a-zA-Z]", "").toLowerCase();
                    if (word != "") {
                        if (wordCountMap.containsKey(word)) {
                            wordCountMap.put(word, wordCountMap.get(word) + 1);
                        } else {
                            wordCountMap.put(word, 1);
                        }
                    }
                }
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                reader.close();
            }
        }
        Entry<String, Integer>[] entryArray = (Entry<String, Integer>[])wordCountMap.entrySet()).toArray();
        Arrays.sort(entryArray, new Comparator<Entry<String, Integer>>() {
            public int compare(Entry<String, Integer> entry1, Entry<String, Integer> entry2) {
                return entry2.getValue() - entry1.getValue();
            }
        });
        for (int i = 0; i < Math.min(entryArray.length, 10); i++) {
            System.out.println(entryArray[i].getKey() + ": " + entryArray[i].getValue());
        }
    }
}
