import re

html = '''
<div id="{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
" style="background-color: orange;">
    Content with orange background color
</div>
'''

element_id = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

pattern = fr'<div[^>]*id="{element_id}"[^>]*style="[^"]*background-color:\s*orange[^"]*"[^>]*>'
match = re.search(pattern, html)

if match:
    print(f"The element with ID '{element_id}' has an orange background color.")
else:
    print(f"The element with ID '{element_id}' does not have an orange background color.")
