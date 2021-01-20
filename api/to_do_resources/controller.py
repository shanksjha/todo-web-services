from flask import Blueprint,jsonify,request
from api.data.models import Bucket,ToDoDetails

to_do_services = Blueprint('to_do_services',__name__)


@to_do_services.route('/get_buckets',methods=['GET'])
def get_buckets():
    bucket_details = Bucket.get_bucket_details()
    final_response= []
    for bucket_id,bucket_name,todo_id,todo_name,todo_status in bucket_details:
        if bucket_id in (a['bucket_id'] for a in final_response if a != None):
            dict_to_get = [a for a in final_response if a['bucket_id'] == bucket_id][0]
            dict_to_get['todo_list'].append({'todo': todo_id,'todo_name':todo_name,'todo_status':todo_status})
        else:
            final_response.append({
                'bucket_id': bucket_id,
                'bucket_name':bucket_name,
                'todo_list': [{
                    'todo_id': todo_id,
                    'todo_name': todo_name,
                    'todo_status': todo_status
                }]
            })

    return jsonify(final_response)


@to_do_services.route('/create_bucket',methods=['POST'])
def create_bucket():
    request_body = request.json
    bucket_name = request_body['bucket_name']
    bucket_obj = Bucket(bucket_name)
    Bucket.create_bucket(bucket_obj)
    return get_buckets()


@to_do_services.route('/create_todo',methods=['POST'])
def create_todo():
    request_body = request.json
    bucket_id = request_body['bucket_id']
    to_do_name = request_body['to_do_name']
    to_do_obj = ToDoDetails(to_do_name,bucket_id)
    ToDoDetails.create_todos(to_do_obj)
    return get_buckets()


@to_do_services.route('/update_todo/<todo_id>',methods=['PUT'])
def update_todo(todo_id):
    print(request.json['todo_status'])
    print(todo_id)
    ToDoDetails.update_todo(todo_id, request.json['todo_status'])
    return get_buckets()






