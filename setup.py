#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-family-central.jarbasai=skill_family_central:FamilyCentralSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-family-central',
    version='0.0.1',
    description='ovos classic family family skill plugin',
    url='https://github.com/JarbasSkills/skill-family-central',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_family_central": ""},
    package_data={'skill_family_central': ['locale/*', 'res/*']},
    packages=['skill_family_central'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
