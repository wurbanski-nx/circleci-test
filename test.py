import yaml

print yaml.dump({'hello': 'world', 'iam':{'groot': 'iamgroot'}},
                default_flow_style=False)
