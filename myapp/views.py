from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore

def home(request):
    return render(request, 'myapp/home.html')
from firebase_admin import firestore
import json

def add_task(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from request body
            print("Received POST request")
            task_data = json.loads(request.body)
            print("Task data:", task_data)
            
            # Get reference to Firestore database
            db = firestore.client()
            # Check if document exists
            doc_ref = db.collection('tasks').document(task_data['document_id'])
            doc = doc_ref.get()
            if not doc.exists:
                print(f"Creating new document with ID: {task_data['document_id']}")
            else:
                print(f"Document {task_data['document_id']} already exists, updating content")
            # Add task to 'tasks' collection
            db.collection('tasks').document(task_data['document_id']).set({
                'description': task_data['description'], 
                'priority': task_data['priority'],
                'done': task_data['done']
            })
            print("Task added to Firestore successfully")
            
            return JsonResponse({'status': 'success', 'message': 'Task added successfully', 'task_id': task_data['document_id']})
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
    return render(request, 'myapp/add_task.html')

def view_task(request):
    return render(request, 'myapp/view_task.html')

def get_all_tasks(request):
    try:
        db = firestore.client()
        tasks_ref = db.collection('tasks')
        tasks = tasks_ref.stream()
        
        tasks_list = []
        for task in tasks:
            task_data = task.to_dict()
            # Add the document ID to the task data
            task_data['name'] = task.id  # This adds the document ID as the name
            tasks_list.append(task_data)
        
        return JsonResponse({
            'status': 'success',
            'tasks': tasks_list
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

def search_task(request):
    try:
        task_name = request.GET.get('name')
        if not task_name:
            return JsonResponse({
                'status': 'error',
                'message': 'Task name is required'
            })

        db = firestore.client()
        tasks_ref = db.collection('tasks')
        # Get the specific document directly using document ID
        doc_ref = tasks_ref.document(task_name)
        doc = doc_ref.get()
        
        tasks_list = []
        if doc.exists:
            task_data = doc.to_dict()
            task_data['name'] = doc.id  # Add the document ID as the name
            tasks_list.append(task_data)
        
        return JsonResponse({
            'status': 'success',
            'tasks': tasks_list
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

def suggestions(request):
    return render(request, 'myapp/suggestions.html')

