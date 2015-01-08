from m2re.settings import *

print 'Usando local_settings'
DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS += (
    'applications.context_processors.send_debug_to_template',
)
