import jinja2
import os
import re
import subprocess
latex_jinja_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath('.')))

template = latex_jinja_env.get_template('./graphic_template_2_waves.tex')
for file in os.listdir('.'):
    if(re.match('.+\.csv$',file)):
        tmp_file = template.render(filename=file)
        file = file[0:len(file)-4]
        with open(file + ".template", 'w') as f:
            f.write(tmp_file)

        subprocess.call(["pdflatex", file + ".template"])
