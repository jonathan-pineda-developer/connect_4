#hello world in python



def Response():
    response = True
    if response:
        return True
    else:
        return False
    
def evaluateResponse(response):
    if response:
        return"Response is True"
    else:
        return"Response is False"
  

def main():
    response = Response()
    print(response)
    result = evaluateResponse(response)
    print(result)

if __name__ == "__main__":
    main()


