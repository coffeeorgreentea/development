import banana_dev as banana
model_inputs = {
 'code': open('code.py','r').read()
}
api_key = "REDACTED"
model_key = "REDACTED"
for x in range(0,10):
    out = banana.start(api_key, model_key, model_inputs)
    print(out)