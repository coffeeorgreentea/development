
import banana_dev as banana


model_inputs = {
  'code': 'x = 5\ny = 2\nresponse = x * y',
#  An alternative is to read in a file directly  
#  'code': open('code.py','r').read()
}

api_key = "YOUR_API_KEY"
model_key = "YOUR_MODEL_KEY"

out = banana.run(api_key, model_key, model_inputs)
print(out)


