import requests
from requests.auth import HTTPBasicAuth
#-----------------------------------------------------------------------------------------#
api_key = '9b051c870442e82e4ac11c1bed2dccd897996f4e'
source_file = "tmp/armash.pdf"
target_file = "results/armash.txt"
target_format = "txt"
#-------------------------------------------------------------------------------------------#



def check(job_id,api_key):
	check_endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
	response = requests.get(check_endpoint, auth=HTTPBasicAuth(api_key, ''))
	#print(response.json())
	#print(response.json())
	checked_data=response.json()
	value_list=checked_data['target_files']
	#print(value_list[0]['id'])
	return value_list[0]['id']

def download(file_id,api_key,local_filename):
	downlaod_endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)
	download_response = requests.get(downlaod_endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))
	try:
	  with open(local_filename, 'wb') as f:
	    for chunk in download_response.iter_content(chunk_size=1024):
	      if chunk:
	        f.write(chunk)
	        f.flush()

	    print("File downloaded")

	except IOError:
	  print("Error")


endpoint = "https://sandbox.zamzar.com/v1/jobs"
file_content = {'source_file': open(source_file, 'rb')}
data_content = {'target_format': target_format}
res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
print(res.json())
data=res.json()
#print(data)
print("=========== Job ID ============\n\n")
print(data['id'])
target_id=check(data['id'],api_key)
print("\n================= target_id ===========\n\n")
print(target_id)
download(target_id,api_key,target_file)