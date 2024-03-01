# Import necessary libraries
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Import required modules
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#get gemini response
def get_gemini_response(input,job_dec,resume_content):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([input,job_dec,resume_content])
    return response.text


# Load PDF using PyPDFLoader
loader = PyPDFLoader("./data/PriyanshuDixit_Resume.pdf")
pages = loader.load_and_split()

# Initialize RecursiveCharacterTextSplitter with specified parameters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=True,
)

# Split the text content of the first page into chunks
chunks = text_splitter.split_text(pages[0].page_content)

# Concatenate all the chunks into a single text
resume_content = ""
for chunk in chunks:
    resume_content += chunk

# Print the final concatenated text

input_prompt = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

job_dec="""

Solid understanding of React, comfortable with the latest versions, and expertise in writing composable,
testable, and reusable components.
● Minimum 2 years of experience in software development, with strong expertise in front-end development.
● Hands on experience with React hooks and custom hooks.with understanding on Typescript.
● Strong in Javascript, HTML & SCSS and hands-on with ES6
● Strong problem-solving abilities and analytical skills, ability to take ownership as appropriate
● Excellent communication and coordination skills and willing to learn new skills
● Experience working on GIT, must adhere to commit standards and implement best coding practices & coding structure.
● Must be familiar with CI/CD deployment process and have willingness to write pipelines.

"""

response=get_gemini_response(input_prompt,job_dec,resume_content)
print(response)