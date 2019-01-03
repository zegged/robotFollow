## *********************************************************
##
## File autogenerated for the roboteq_control package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 290, 'description': 'Configuration encoder', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'configuration', 'edit_method': "{'enum_description': 'configuration', 'enum': [{'srcline': 9, 'description': 'Unused', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'unused'}, {'srcline': 10, 'description': 'Command', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'command'}, {'srcline': 11, 'description': 'Feedback', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'feedback'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': 'Configuration pulse input', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'input_motor_one', 'edit_method': "{'enum_description': 'Enable feedback from this motor', 'enum': [{'srcline': 14, 'description': 'Disabled', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'disabled'}, {'srcline': 15, 'description': 'enabled', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'enabled'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': 'Configuration pulse input', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'input_motor_two', 'edit_method': "{'enum_description': 'Enable feedback from this motor', 'enum': [{'srcline': 14, 'description': 'Disabled', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'disabled'}, {'srcline': 15, 'description': 'enabled', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'enabled'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': '[#] An Integer parameter', 'max': 5000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'PPR', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': 'Position encoder respect to gears', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'position', 'edit_method': "{'enum_description': 'Position', 'enum': [{'srcline': 22, 'description': 'After gears', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'After'}, {'srcline': 23, 'description': 'Before gears', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqEncoder.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Before'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': '[#] Encoder minimum count value', 'max': 2147000000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'encoder_low_count_limit', 'edit_method': '', 'default': -1000, 'level': 0, 'min': -2147000000, 'type': 'int'}, {'srcline': 290, 'description': '[#] Encoder maximum count value', 'max': 2147000000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'encoder_high_count_limit', 'edit_method': '', 'default': 1000, 'level': 0, 'min': -2147000000, 'type': 'int'}, {'srcline': 290, 'description': '[#] Encoder home count', 'max': 2147000000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'encoder_home_count', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2147000000, 'type': 'int'}, {'srcline': 290, 'description': 'Load all parameters from Roboteq board', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'load_roboteq', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': 'Restore to the original configuration', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'restore_defaults', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

RoboteqEncoder_unused = 0
RoboteqEncoder_command = 1
RoboteqEncoder_feedback = 2
RoboteqEncoder_disabled = 0
RoboteqEncoder_enabled = 1
RoboteqEncoder_After = 0
RoboteqEncoder_Before = 1
