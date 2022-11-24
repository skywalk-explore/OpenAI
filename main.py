from flask import Flask, request, render_template
import openai

app = Flask(__name__)

def openAi(prompt):
    openai.api_key = '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'
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=str(prompt),
        temperature=0.1,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,)
    return response.choices[0]['text'].splitlines()

@app.route('/', methods=['GET', 'POST'])
def iNeedHelpWith():
    if request.method == 'POST':
        # getting formData selection from help.html page
        formData = request.form.get('Request')
        # passing the formData to the OpenAi function to undertake it's work
        response = openAi(formData)
        # the formData text is a key within the dictionary below that links to a link
        return render_template('home.html', response=response)
    if request.method == 'GET':
        return render_template('home.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)