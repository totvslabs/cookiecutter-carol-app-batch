{%-if cookiecutter.pycarol_version == 'latest' %}
FROM totvslabs/pycarol:latest
{%- else %}
FROM totvslabs/pycarol:{{ cookiecutter.pycarol_version }}
{%- endif %}

env SRCFOLDER={{cookiecutter.project_slug}}

WORKDIR /app
ADD requirements.txt /app/
ADD $SRCFOLDER/* /app/

RUN pip install -r requirements.txt

VOLUME [ "/app" ]

CMD ["python3", "-m", "{{cookiecutter.algorithm_name}}.py"]
