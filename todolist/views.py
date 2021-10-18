from django.shortcuts import render, redirect
from .models import TodoList, Project




def index(request):         #the index view
    todos = TodoList.objects.all()          #quering all todos with the object manager
    projects = Project.objects.all()     #getting all categories with object manager


    if request.method == "POST":            #checking if the request method is a POST

        if "taskAdd" in request.POST:       #checking if there is a request to add a todo
            title = request.POST["description"]     #title
            date = str(request.POST["date"])    #date
            project = request.POST["category_select"]          #category
            content = title + " -- " + date + " " + project    #content
            todo = TodoList(title=title, content=content, due_date=date, project=Project.objects.get(name=project))
            todo.save() #saving the todo
            return redirect("projectlist") #reloading the page

        if "taskDelete" in request.POST:        #checking if there is a request to delete a _todo
            if request.POST.get("taskCheckbox"):
                checkedlist = request.POST.getlist("taskCheckbox")     #checked todos to be deleted

                for todo_id in checkedlist:

                    todo = TodoList.objects.get(id=int(todo_id))    #getting _todo id
                    todo.delete()   #deleting _todo
            else:
                pass

        if "projectDelete" in request.POST:        #checking if there is a request to delete a _project
            if request.POST.get("projectCheckbox"):

                projectlist = request.POST.getlist("projectCheckbox")     #checked _project to be deleted

                for project_id in projectlist:
                    print(project_id)

                    proj = Project.objects.get(name=(project_id))    #getting _project id
                    print(proj)
                    proj.delete()   #deleting _project
            else:
                pass

        if "projectADD" in request.POST:  # checking if there is a request to delete a _todo
            name = request.POST["projectName"]
            ProjectItem = Project(name=name)
            ProjectItem.save()
            return redirect("projectlist")  # reloading the page


    context = { "projects": projects}

    return render(request, "todolist/categories.html", context)























# def categories(request):         #the index view
#     todos = TodoList.objects.all()          #quering all todos with the object manager
#     categories = Category.objects.all()     #getting all categories with object manager
#     # form = ProjectForm()                    #defining form
#
#     if request.method == "POST":            #checking if the request method is a POST
#
#         if "taskAdd" in request.POST:       #checking if there is a request to add a todo
#             title = request.POST["description"]     #title
#             date = str(request.POST["date"])    #date
#             category = request.POST["category_select"]          #category
#             content = title + " -- " + date + " " + category    #content
#             Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
#             Todo.save() #saving the todo
#             return redirect("projectlist") #reloading the page
#
#         if "taskDelete" in request.POST:        #checking if there is a request to delete a _todo
#             if request.POST.get("checkedbox"):
#                 checkedlist = request.POST["checkedbox"]     #checked todos to be deleted
#                 for todo_id in checkedlist:
#                     todo = TodoList.objects.get(id=int(todo_id))    #getting _todo id
#                     todo.delete()   #deleting _todo
#             else:
#                 pass
#
#         if "projectADD" in request.POST:  # checking if there is a request to delete a _todo
#             name = request.POST["projectName"]
#             ProjectItem = Category(name=name)
#             ProjectItem.save()
#             return redirect("projectlist")  # reloading the page
#
#
#     context = { "todos": todos, "categories": categories}
#
#     return render(request, "todolist/categories.html", context)