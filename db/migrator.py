import argparse
import logging
from jinja2 import Environment, FileSystemLoader

LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Generates a SQL migration file from a jinja2 template."
)
parser.add_argument(
    "-db",
    "--database",
    type=str,
    required=True,
    help="The name of the database we are applying this migration on.",
)
parser.add_argument(
    "-t",
    "--template",
    type=str,
    required=True,
    help="The file name of the jinja2 template to compile.",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    required=True,
    help="The file name of the compiled (output) template.",
)

args = parser.parse_args()

try:

    with open(args.template) as f:
        template_str = f.read()

    template = Environment(loader=FileSystemLoader(".")).from_string(template_str)
    rendered = template.render(database=args.database)

    output_file = open(f'{args.output}', 'w')
    output_file.write(rendered)
    output_file.close()
        
except Exception as cause:
    LOGGER.error(
        f"Migration template generation failed with exception",
        exc_info=True,
    )
    raise cause









