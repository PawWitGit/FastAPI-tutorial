"""Task 1"""

# #filename main.py
#
# from fastapi import FastAPI, HTTPException, status, Depends
#
# development_db = ["DB for Development"]
#
# def get_db_session():
#     return development_db
#
# app = FastAPI()
#
#
# @app.get("/add-item/")
# def add_item(item:str, db = Depends(get_db_session)):
#     db.append(item)
#     print(db)
#     return {"message":f"added item {item}"}

"""Task 2"""

from fastapi import FastAPI, Depends

app = FastAPI()

dummy_db = {
    "1": "SDE1 at google.com",
    "2": "SDE2 at Amazon",
    "3": "Backend Dev. at Spotify",
    "4": "Senior Engineer at Alphabet",
    "5": "Devops Eng. at Microsoft",
}


class GetObjectOrFeatured:
    """We let promote their jobs"""

    def __init__(self, featured_job: str):
        self.featured_job = featured_job

    def __call__(self, id: str) -> str:
        value = dummy_db.get(id)
        if not value:
            value = dummy_db.get(self.featured_job)
        return value


@app.get("/job/{id}")
def get_job_by_id(job_title: str = Depends(GetObjectOrFeatured("2"))):
    return job_title
