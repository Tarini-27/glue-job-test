import json, os
import boto3, zipfile
import subprocess
s3_client = boto3.client('s3')
glue_client = boto3.client('glue')

def create_glue_job(fun_name):
    base_func_name = fun_name.split('.')
    base_func_name = base_func_name[0]
    response = glue_client.create_job(
        Name= base_func_name,
        Role='arn:aws:iam::130159455024:role/SunLifeCyberSecurity-Developer-3857',
        ExecutionProperty={
            'MaxConcurrentRuns': 123
        },
        Command={
            'Name': 'glueetl',
            'ScriptLocation': 's3://sunlife-cybersec-test/Glue/'+fun_name+'.py',
            'PythonVersion': '3'
        },
        
    )
    return response

def update_glue_job(fun_name):
    response = glue_client.update_job(
        JobName= fun_name,
        JobUpdate={
            'Role': 'arn:aws:iam::130159455024:role/SunLifeCyberSecurity-Developer-3857',
            'ExecutionProperty': {
                'MaxConcurrentRuns': 123
            },
            'Command': {
                'Name': 'glueetl',
                'ScriptLocation': 's3://sunlife-cybersec-test/Glue/'+fun_name+'.py',
                'PythonVersion': '3'
            }
        }
    )
    return response

def get_glue_job(fun_name):
    response = glue_client.get_job(
        JobName=fun_name
    )
    return response

def run_glue_job(fun_name):
    response = glue_client.start_job_run(
        JobName=fun_name,
    )
    return response

def handler():
    name1 = os.environ['name1']
    file_name = name1.split(' ')
    print(file_name)
    allowed_files = ["sunlife-aman-glue-test.py","Sunlife_cyber_sec_test_1.py"]
    for name in file_name:
        if name in allowed_files:
            # fun_name = name.split('.')
            # fun_name = fun_name[0]
            # print(fun_name)
            try:
                print("Testing")
                res = subprocess.run(["docker", "run", "--name", "glue-container", "glue-image"])
                print(res)
                print(res.returncode)
                if res.returncode==0:
                    print("Test Passed")
                else:
                    print("Test Failed")
                    raise Exception("Test Failed")
            except Exception as e:
                print("Error in testing",e)
                return
            try:
                # zip_file = zipfile.ZipFile(fun_name+'.zip','w')
                # zip_file.write(name,compress_type=zipfile.ZIP_DEFLATED)
                # zip_file.close()
                response = s3_client.upload_file(name, 'sunlife-cybersec-test', 'Glue/'+name)
                # print(response)
                

            except Exception as e:
                print("Error While uploading to s3")
                return False

            base_func_name = name.split('.')
            base_func_name = base_func_name[0]
            try:
                res = get_glue_job(base_func_name)
                if res:
                    print("Updating boto3 job")
                    response = update_glue_job(base_func_name)
                    print(response)
                    if response:
                        print("Running glue job")
                        # res1 = run_glue_job(base_func_name)
                        # print(res1)
            except Exception as e:
                print("Glue job not present")
                print("Creating a new glue job")
                response = create_glue_job(base_func_name)
                print(response)
                if response:
                    print("Running glue job")
                    # res1 = run_glue_job(base_func_name)
                    # print(res1)

            
handler()
