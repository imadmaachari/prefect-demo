from prefect import flow, task
from prefect.blocks.system import String

string_block = String.load("db-credentials")

@task
def create_message():
    msg = string_block.value
    return(msg)
@flow
def something_else():
    result = 10
    return(result)
    
@flow
def hello_world():
    subflow_message = something_else()
    task_msg = create_message()
    new_message = task_msg + str(subflow_message)
    print(new_message)
    
if __name__ == "__main__":
    hello_world()