# Terraform
Terraform is an infrastructure as code tool that enables you to safely and predictably provision and manage infrastructure in any cloud.

| |Index|
|---|---|
|1|[Install](#install)|
|2|[Config](#config)|
|3|[Command](#command)|

![Terraform](https://github.com/barneywill/bigdata_demo/blob/main/imgs/terraform_architecture.jpg)

## 1 <a id='install'></a>Install
```
https://developer.hashicorp.com/terraform/install

wget https://releases.hashicorp.com/terraform/1.10.3/terraform_1.10.3_linux_amd64.zip
unzip terraform_1.10.3_linux_amd64.zip
sudo mv terraform /usr/local/bin

terraform version
```

## 2 <a id='install'></a>Config
<a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/terraform/main.tf'>main.tf</a>

## 3 <a id='install'></a>Command
```
terraform init

terraform plan

terraform apply

terraform destroy
```

