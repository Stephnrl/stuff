import importlib.util
import json
import pathlib
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'plugins/mux-brief/skills/mux-brief/scripts/brief.py'
spec=importlib.util.spec_from_file_location('mux_brief', SCRIPT)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class BriefTests(unittest.TestCase):
    def test_render_structure(self):
        text=mod.render({'target':'copilot-cli','mode':'investigate','outcome':'Identify CI failure',
                         'scope':['Read logs'],'evidence':['Quote failure lines']})
        self.assertIn('Outcome: Identify CI failure',text)
        self.assertIn('Scope:',text)
        self.assertNotIn('Approval gate:',text)

    def test_operate_adds_gate(self):
        text=mod.render({'mode':'operate','outcome':'Inspect deployment status'})
        self.assertIn('Approval gate:',text)

    def test_secret_refusal(self):
        with self.assertRaises(ValueError):
            mod.render({'outcome':'Analyze this token ghp_'+'a'*36})

    def test_bad_types(self):
        with self.assertRaises(ValueError):
            mod.render({'outcome':'ok','scope':'all'})

    def test_canonical_example(self):
        path=ROOT/'plugins/mux-brief/skills/mux-brief/assets/brief.example.json'
        output=mod.render(json.loads(path.read_text()))
        self.assertIn('Stop before changing runners',output)

if __name__=='__main__':
    unittest.main()
