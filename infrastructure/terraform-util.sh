
#!/bin/sh
init_config()
{
    export TF_VAR_project=cb-dataflow-python
    export TF_VAR_region=australia-southeast1
    export TF_VAR_env=dev
    export GOOGLE_CLOUD_KEYFILE_JSON=/Users/karthikeysurineni/dataflow-python/cb-dataflow-python-23cc97500072.json
    export GOOGLE_APPLICATION_CREDENTIALS=/Users/karthikeysurineni/dataflow-python/cb-dataflow-python-23cc97500072.json
}

init()
{
    echo "Initializing Backend"
    declare BACKEND_BUCKET=tf-state-cb-dataflow-python-dev
    declare BACKEND_PREFIX=terraform-remote-state
    init_config
    terraform init \
    -backend-config="bucket=${BACKEND_BUCKET}" \
    -backend-config="prefix=${BACKEND_PREFIX}"
}

plan()
{
    init_config
    terraform plan
}
apply()
{
    init_config
    terraform apply --auto-approve
}
destroy(){
    init_config
    terraform destroy --auto-approve
}

"$@"