{%-if cookiecutter.pycarol_version == 'latest' %}
FROM totvslabs/pycarol:latest
{%- else %}
FROM totvslabs/pycarol:{{ cookiecutter.pycarol_version }}
{%- endif %}


WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD {{cookiecutter.project_slug}}/ /app/{{cookiecutter.project_slug}}/

VOLUME [ "/app" ]

CMD ["python3", "-m", "{{cookiecutter.project_slug}}.{{cookiecutter.algorithm_name}}"]
