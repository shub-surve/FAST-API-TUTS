from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI(title="Affrmtn")

blogs = {
    "1": "I am going to be rich",
    "2": "Ill be in peace",
    "3": "Ill have a great life",
}

people_in_my_life = {
    "1": "NEHA",
    "2": "Kanishka",
    "3": "Prathamesh",
}

def get_blog_or_404(blog_id: str):
    blog = blogs.get(blog_id)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {blog_id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog

@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(get_blog_or_404)):
    return {"blog_id": blog_name}
