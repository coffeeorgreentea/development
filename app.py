def init():
    global model

def inference(model_inputs:dict):
    global model
    local_vars = {}
    if not model_inputs.get('code'):
        return {'error': 'You must supply code for this inference to run.'}
    
    exec(model_inputs.get('code'), globals(), local_vars)

    return local_vars.get('response', {})
