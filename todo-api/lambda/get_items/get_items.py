import json

data = [
    {
        "id": 0,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Finalise Todo app UI and system designs",
        "completed": True,
    },
    {
        "id": 1,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Implement Todo app frontend",
        "completed": False,
    },
    {
        "id": 2,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Draft Todo app AWS infrastructure as IaC",
        "completed": False,
    },
    {
        "id": 3,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Implement CRUD Lambdas for Todo app",
        "completed": False,
    },
    {
        "id": 4,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Hook up Todo app frontend to backend via API Gateway and Next.js API routes",
        "completed": False,
    },
    {
        "id": 5,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Run a full test of Todo app",
        "completed": False,
    },
    {
        "id": 6,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Fix bugs and clean up code",
        "completed": False,
    },
    {
        "id": 7,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Create documentation for Todo app",
        "completed": False,
    },
    {
        "id": 8,
        "date": "2023-11-26T10:10:22.296Z",
        "description": "Bask in glory!",
        "completed": False,
    },
]


def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"data": data}),
    }
