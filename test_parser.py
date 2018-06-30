import parser


class TestParser:
    def test_node_to_json(self):
        node = parser.Node(value=parser.Node.Ops.AND.value, left=parser.Node(value='HEY'), right=parser.Node(value='HO'))
        assert node.to_dict() == {'value': '&', 'left': {'value': 'HEY', 'left': None, 'right': None}, 'right': {'value': 'HO', 'left': None, 'right': None}}

    def test_parse(self):
        tree = parser.parse('CS2020 & CS 2022')
        assert tree == parser.Node.Ops.AND
        assert tree.right == 'CS2020'
        assert tree.left == 'CS2022'

    def test_make_tree(self):
        tree = parser.make_tree(iter('||DB&BA'))
        assert parser.Node.Ops.OR == tree
        assert tree.left == parser.Node.Ops.OR
        assert tree.right == parser.Node.Ops.AND

    def test_polish_notation(self):
        assert parser.convert_polish_notation('(0|(1&2))&2') == '&2|&210'
        assert parser.convert_polish_notation('0&1') == '&10'
        assert parser.convert_polish_notation('((A&B)|C|D)') == '||DC&BA'