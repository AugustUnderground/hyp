import setuptools
 
package_name = 'hyp'

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as req:
    requirements = req.read().splitlines()
 
setuptools.setup( name                          = package_name
                , version                       = '0.0.2'
                , author                        = 'Yannick Uhlmann'
                , author_email                  = 'augustunderground@protonmail.com'
                , description                   = 'Boilerplate project directory setup'
                , long_description              = long_description
                , long_description_content_type = 'text/markdown'
                , url                           = 'https://github.com/augustunderground/hyp'
                , packages                      = setuptools.find_packages()
                , classifiers                   = [ 'Development Status :: 2 :: Pre-Alpha'
                                                  , 'Programming Language :: Python :: 3'
                                                  , 'Operating System :: POSIX :: Linux' ]
                , python_requires               = '>=3.8'
                , install_requires              = requirements
                , entry_points                  = { 'console_scripts': [ 'hyp = hyp.__main__:main' ]}
                , package_data                  = { '': ['*.hy', '__pycache__/*']}
                #, data_files                    = [ ('share/man/man1', ['doc/hyp.1'])
                #                                  , ('share/man/man8', ['doc/hyp.8'])]
                , )
