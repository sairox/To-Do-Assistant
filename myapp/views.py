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
            
            # Add task to 'tasks' collection
            db.collection('tasks').document(task_data['name']).set({
                'description': task_data['description'], 
                'priority': task_data['priority'],
                'done': task_data['done']
            })
            print("Task added to Firestore successfully")
            
            return JsonResponse({'status': 'success', 'message': 'Task added successfully', 'task_id': task_data['name']})
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
    return render(request, 'myapp/add_task.html')

def view_task(request):
    return render(request, 'myapp/view_task.html')

def suggestions(request):
    return render(request, 'myapp/suggestions.html')

