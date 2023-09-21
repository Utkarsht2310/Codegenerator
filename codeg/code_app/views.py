from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
def index(request):
    return render(request,"main/index.html")


import openai

def generate_code(description, language):
    openai.api_key = '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'
    
    # Define your prompt for GPT-3
    prompt = f"Generate code in {language} for: {description}"
    
    # Make an API call to generate code
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose an appropriate engine
        prompt=prompt,
        max_tokens=100,  # Adjust the token limit as needed
        n=1  # You can experiment with different values
    )

    # Extract the generated code from the response
    generated_code = response.choices[0].text

    return generated_code



def code_generation_view(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        language = request.POST.get('language')

        generated_code = generate_code(description, language)

        # Render the generated code in your template
        return render(request, 'main/result.html', {'generated_code': generated_code})
    else:
        # Handle GET requests (render the form)
        return render(request, 'main/index.html')
