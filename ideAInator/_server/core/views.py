from django.shortcuts import render, redirect
from django.conf import settings
import json
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import myUser, ChatLog
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
# from .models import PDFUpload, ChatLog
# from utils.pdf_parser import PDF_parser
from django.core.files.storage import default_storage 
from .utils import pdf_parser
from .utils import text_processor
from openai import OpenAI
from .keys import api_key
from .utils import chatgptSecurity
from django.contrib.auth import get_user_model
from .models import ExtractedText


User = get_user_model()

# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f"{settings.BASE_DIR}/core/static/manifest.json")
    MANIFEST = json.load(f)

# Create your views here.
@login_required
def index(req):
    context = {
        "asset_url": os.environ.get("ASSET_URL", ""),
        "debug": settings.DEBUG,
        "manifest": MANIFEST,
        "js_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["file"],
        "css_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["css"][0]
    }
    return render(req, "core/index.html", context)

@login_required
def home(req):
    return JsonResponse({"success": True })


@login_required
def chat(req):
    return JsonResponse({"success": True })



@csrf_exempt
@login_required
def profile_view(request):
    if request.method == "GET":
        # Retrieve the current user's profile data
        user = request.user
        
        # Get the class names from ExtractedText and assign them to the profile
        classes = [entry.class_name for entry in ExtractedText.objects.all()]
        
        # Return the current user's profile data, including the classes
        return JsonResponse({
            "display_name": user.first_name,
            "classes": classes,  # Include the extracted class names here
            "conversations": user.conversations  # Assuming you have this data to return
        })
    
    elif request.method == "PUT" or request.method == "POST":
        # Update the user's profile data
        data = json.loads(request.body)
        user = request.user
        user.classes = data.get("classes", user.classes)
        user.conversations = data.get("conversations", user.conversations)
        user.save()
        return JsonResponse({"success": True, "message": "Profile updated successfully!"})

@csrf_exempt
def save_conversation(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid HTTP method. Use POST."}, status=405)

    try:
        data = json.loads(request.body)
        print(data)
        new_conversation = data.get("conversation")

        print("ok 1")
        if not new_conversation:
            return JsonResponse({"error": "No conversation data provided."}, status=400)
        print("ok 2")
        # Use request.user directly
        user = request.user
        
        # Assuming conversations is a JSONField in your CustomUser model
        if not isinstance(user.conversations, list):
            user.conversations = []
        
        user.conversations.append(new_conversation)
        user.save()
        
        return JsonResponse({
            "success": True, 
            "message": "Conversation saved successfully.",
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data."}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
    
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        file_path = default_storage.save(f"temp/{uploaded_file.name}", uploaded_file)
        parser = pdf_parser.PDF_parser.create_instance(file_path)
        extracted_text = parser.convert_pdf()
        class_name = parser.get_class_and_semester()
        os.remove(file_path)

        # Save to database
        record = ExtractedText.objects.create(text=extracted_text, class_name=class_name)
        

        return JsonResponse({
            'message': 'File processed successfully',
            "record_id": record.id,  # Return the record ID for later retrieval
            "extracted_text": extracted_text[:100]  # Send a snippet of extracted text
        })

    return JsonResponse({'error': 'No file uploaded'}, status=400)

def getSurveyData(request):
    # Retrieve the most recent extracted text
    try:
        latest_record = ExtractedText.objects.latest('created_at')  # Fetch the latest entry
        print(latest_record.text)
        return latest_record.text
    except ExtractedText.DoesNotExist:
        return JsonResponse({'error': 'No survey data available'}, status=404)



@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            # Parse the JSON body from the request
            body = json.loads(request.body)
            user_message = body.get("text", "")  # Get the user's message

            if not user_message:
                return JsonResponse({"error": "No message provided."}, status=400)

            # Generate an AI response (placeholder logic)
            ai_response = f"{get_chatGPT_response(request, user_message)}"  # Replace with your AI logic

            # Return the AI response as JSON
            return JsonResponse({"response": ai_response})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

    # If not a POST request, return a method not allowed response
    return JsonResponse({"error": "Method not allowed."}, status=405)



def get_chatGPT_response(request, user_message):
    if chatgptSecurity.is_inappropriate_input(user_message):
        return "I cannot assist with that. I am here to help improve teaching and learning."

    client = OpenAI(api_key=api_key,)

    prompt=f"""
    You are a helpful assistant. I am a teacher at a university.
    With the following student survey data, answer the prompt below:
    {user_message}.
    \n\n
    {getSurveyData(request)}. 
    You are **only allowed to** assist with improving teaching or related academic matters.
    Do not engage in, encourage, or provide information about illegal, unethical, or harmful activities such as phishing, bomb-making, or anything unrelated to teaching improvement.
    If the user asks about something inappropriate, your response should be: "I cannot assist with that. I am here to help improve teaching and learning."
    Your response should always be constructive, educational, and within the bounds of ethical conduct.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    r=response.choices[0].message.content
    #check if output is appropraite
    if chatgptSecurity.is_inappropriate_output(r):
        return "I cannot assist with that. I am here to help improve teaching and learning."
    return r 


@login_required
def transcript_view(request, id):
    try:
        id = int(id)
        # Access the logged-in user's conversations
        user = request.user  # Assumes CustomUser is the AUTH_USER_MODEL
        conversations = user.conversations  # Directly access the conversations field

        # Ensure the conversations field is a list
        if not isinstance(conversations, list):
            return JsonResponse({"error": "Conversations data is not in the correct format."}, status=500)

        # Check if the provided ID is within the valid range
        if id < 0 or id >= len(conversations):
            return JsonResponse({"error": "Conversation not found"}, status=404)

        # Fetch the specific conversation by ID
        conversation = conversations[id]
        return JsonResponse({"conversation": conversation}, status=200)

    except Exception as e:
        # Return a generic error response if something goes wrong
        return JsonResponse({"error": str(e)}, status=500)