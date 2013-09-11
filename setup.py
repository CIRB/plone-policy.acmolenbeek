from setuptools import setup, find_packages

version = '1.0.5'

setup(name='policy.acmolenbeek',
      version=version,
      description="A Plone policy for ac Molenbeek website",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'collective.ckeditor',
          'cirb.zopemonitoring',
          # -*- Extra requirements: -*-
          'plonetheme.acmolenbeek',
          'collective.anysurfer',
          'collective.portlet.videoanysurfer',
          'collective.videoanysurfer',
          'collective.easyslider',
          'collective.gallery',
          'collective.galleriffic',
          'collective.quickupload',
          'Solgema.fullcalendar',
          'collective.js.innerfade',
          'Products.PloneFormGen',
          'quintagroup.analytics',
          'collective.checktranslated',
          'collective.languagemovefolders',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
