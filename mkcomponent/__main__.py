import os
import sys
from pathlib import Path


def main():
    component_name = sys.argv[1]
    component_split_name = component_name.split('-')

    total = len(component_split_name)
    if total > 1:
        component_updated_name = ''
        for i in component_split_name:
            component_updated_name += i.capitalize()
    else:
        component_updated_name = component_split_name[0].capitalize()

    style_type = sys.argv[2].capitalize()
    cur_path = os.getcwd()
    new_path = cur_path + '/components/' + component_name + '/'
    print(f"Creating the {component_name} component")
    Path(new_path).mkdir(parents=True)
    f_index = open(new_path + 'index.jsx', 'w')
    f_styles = open(new_path + 'styles.js', 'w')
    f_export = open(cur_path + '/components/' + 'index.js', 'a')

    f_index.write(
        f'import {{ {style_type} }} from \'./styles\';\n'
        f'\n'
        f'const {component_updated_name} = () => <{style_type}>children</{style_type}>;\n'
        f'\n'
        f'export default {component_updated_name};\n'
    )
    f_index.close()

    f_styles.write(
        f'import styled from \'styled-components\';\n'
        f'\n'
        f'export const {style_type} = styled.div``;\n'
    )
    f_styles.close()

    f_export.write(
        f'export {{ default as {component_updated_name} }} from \'./{component_name}\';\n'
    )
    f_export.close()
    print('Done')


if __name__ == '__main__':
    main()
