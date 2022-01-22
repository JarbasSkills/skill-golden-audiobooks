#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-golden-audiobooks.jarbasai=skill_golden_audiobooks:GoldenAudioBooksSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-golden-audiobooks',
    version='0.0.1',
    description='ovos skill_golden_audiobooks skill plugin',
    url='https://github.com/JarbasSkills/skill-golden-audiobooks',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_golden_audiobooks": ""},
    package_data={'skill_golden_audiobooks': ['locale/*', 'res/*', 'ui/*']},
    packages=['skill_golden_audiobooks'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
