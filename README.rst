.. meta::
   :keywords: Teachrine, Toast, Notifier, Battery, Bateria

Theacrine |Theacrine|
=========
| Theacrine é a ferramenta para ajudar a evitar que você esqueça de ligar seu PC na tomada,
  e a bateria se esgote - perdendo todo o trabalho feito... :computer: :battery: :no_entry: :worried:

Installation
============
| Será preciso instalar algumas bibliotecas do Python (e suas dependências), disponíveis no
  `PyPI.org <https://pypi.org>`_: ``PSutil``, ``Win10Toast`` e ``PySimpleGUI``.

Psutil (PyPI)
-------------

|Psutil|

.. code-block:: bash

   pip install psutil

Win10Toast (PyPI)
-----------------

|Win10Toast|

.. code-block:: bash

   pip install win10toast

PySimpleGUI (PyPI)
------------------

|PySimpleGUI|

.. code-block:: bash

   pip install pysimplegui

Ao executar, será apresentado o Painel de Controle:

.. image:: https://github.com/sliatecinos/theacrine/blob/master/Theacrine.PNG

| Escolha o tempo que será monitorado e clique OK.
  Terá as seguintes opções: ``2 hrs``, ``4 hrs``, ``6 hrs`` e ``8 hrs``.
  A opção **Sair** encerra a execução.

Requirements
============
As versões das dependências usadas nesta versão das ferramentas, foram:

* certifi==2021.10.8
* psutil==5.8.0
* pypiwin32==223
* PySimpleGUI
* pywin32==302
* win10toast==0.9
* wincertstore==0.2

Windows
=======
| Poderá ser feita uma versão de arquivo binário (.exe) usando os compiladores disponíveis do Python,
  por exemplo: |pyinstaller| (==4.6), |auto-py-to-exe| (==2.11.0), |cx-Freeze| (==6.8.1 ).


.. |Theacrine| image:: icons/default_32.ico
   :target: https://github.com/sliatecinos/theacrine
   :alt: GitHub - Sliatecinos>Theacrine

.. |PSutil| image:: https://img.shields.io/pypi/dd/psutil?color=yellow&label=psutil&style=plastic
   :target: https://pypi.org/project/psutil/
   :alt: PyPI - Psutil

.. |Win10Toast| image:: https://img.shields.io/pypi/dd/win10toast?color=blue&label=win10toast&style=plastic
   :target: https://pypi.org/project/win10toast/
   :alt: PyPI - Win10Toast

.. |PySimpleGUI| image:: https://img.shields.io/pypi/dd/pysimplegui?color=orange&label=pysimplegui&style=plastic
   :target: https://pypi.org/project/PySimpleGUI/
   :alt: PyPI - PySimpleGUI

.. |pyinstaller| image:: https://img.shields.io/pypi/dm/pyinstaller?color=green&label=pyinstaller
   :target: https://pypi.org/project/pyinstaller/
   :alt: PyPI - pyinstaller

.. |auto-py-to-exe| image:: https://img.shields.io/pypi/dm/auto-py-to-exe?color=red&label=auto-py-to-exe
   :target: https://pypi.org/project/auto-py-to-exe/
   :alt: PyPI - auto-py-to-exe

.. |cx-Freeze| image:: https://img.shields.io/pypi/dm/cx-Freeze?color=informational&label=cx-Freeze
   :target: https://pypi.org/project/cx-Freeze/
   :alt: PyPI - cx-Freeze
