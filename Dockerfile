FROM python:3.9.2 

COPY . . 

RUN pip3 install --no-cache-dir -r requirements.txt 


EXPOSE 9000
CMD ["main.py"] 
ENTRYPOINT ["python3"]

