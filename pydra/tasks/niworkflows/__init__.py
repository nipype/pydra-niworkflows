import attrs
from fileformats.generic import Directory, File
import logging
from pathlib import Path
from pydra.engine import Workflow
from pydra.engine.specs import MultiInputObj
import pydra.mark


logger = logging.getLogger(__name__)



