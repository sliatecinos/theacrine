Theacrine |Theacrine|
=============
Theacrine é a ferramenta para ajudar a evitar que você esqueça de ligar seu PC na tomada, e a bateria se esgote - perdendo todo o trabalho feito... :worried:

Installation
=============
Será preciso instalar alguma bibliotecas do Python, diponíveis no `PyPI.org <https://pypi.org>`_: ``PSutil``, ``Win10Toast`` e ``PySimpleGUI``.

PSutil (PyPI)
----------

|PSutil|

.. code-block:: bash

   pip install psutil
   
Win10Toast (PyPI)
----------

|Win10Toast|

.. code-block:: bash

   pip install win10toast
   
PySimpleGUI (PyPI)
----------

|PySimpleGUI|

.. code-block:: bash

   pip install pysimplegui

Ao executar, será apresentado o Painel de Controle:

.. image:: https://github.com/sliatecinos/theacrine/blob/master/Theacrine.PNG

Escolha do tempo que sera monitorado e clique OK. Tera as opções: ``4 hrs``, ``6 hrs`` e ``8 hrs``.
A opção **Sair** encerra a execução.

Requirements
=============
As versões das dependências usadas nesta versão das ferramentas, foram:

* certifi==2021.10.8
* psutil==5.8.0
* pypiwin32==223
* PySimpleGUI
* pywin32==302
* win10toast==0.9
* wincertstore==0.2


.. |Theacrine| image:: https://github.com/sliatecinos/theacrine/blob/master/thea-leaf-32.ico
   :target: https://github.com/sliatecinos/theacrine
   :alt: PyPI

.. |PSutil| image:: https://img.shields.io/pypi/dd/psutil?color=yellow&label=psutil&style=plastic
   :target: https://pypi.org/project/psutil/
   :alt: PyPI - PSutil
   
.. |Win10Toast| image:: https://img.shields.io/pypi/dd/win10toast?color=blue&label=win10toast&style=plastic
   :target: https://pypi.org/project/win10toast/
   :alt: PyPI - Win10Toast
   
.. |PySimpleGUI| image:: https://img.shields.io/pypi/dd/pysimplegui?color=orange&label=pysimplegui&style=plastic
   :target: https://pypi.org/project/PySimpleGUI/
   :alt: PyPI - PySimpleGUI
