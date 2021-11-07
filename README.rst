.. meta::
   :keywords: Teachrine, Toast, Notifier, Battery, Bateria

Theacrine |Theacrine|
=====================
Theacrine &eacute; a ferramenta para ajudar a evitar que voc&circ; esqueça de ligar seu PC na tomada, e a bateria se esgote - perdendo todo o trabalho feito... :worried:

Installation
============
Ser&aacute; preciso instalar algumas bibliotecas do Python, dipon&iacute;veis no `PyPI.org <https://pypi.org>`_: ``PSutil``, ``Win10Toast`` e ``PySimpleGUI``.

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

Ao executar, ser&aacute; apresentado o Painel de Controle:

.. image:: https://github.com/sliatecinos/theacrine/blob/master/Theacrine.PNG

Escolha do tempo que ser&aacute; monitorado e clique OK. Ter&aacute; as op&ccedil;e&otilde;es: ``4 hrs``, ``6 hrs`` e ``8 hrs``. A opção **Sair** encerra a execução.

Requirements
=============
As vers&otilde;es das depend&circ;ncias usadas nesta vers&atilde;o das ferramentas, foram:

* certifi==2021.10.8
* psutil==5.8.0
* pypiwin32==223
* PySimpleGUI
* pywin32==302
* win10toast==0.9
* wincertstore==0.2


.. |Theacrine| image:: thea-leaf-32.ico
   :target: https://github.com/sliatecinos/theacrine
   :alt: Theacrine - GitHub

.. |PSutil| image:: https://img.shields.io/pypi/dd/psutil?color=yellow&label=psutil&style=plastic
   :target: https://pypi.org/project/psutil/
   :alt: PyPI - Psutil
   
.. |Win10Toast| image:: https://img.shields.io/pypi/dd/win10toast?color=blue&label=win10toast&style=plastic
   :target: https://pypi.org/project/win10toast/
   :alt: PyPI - Win10Toast
   
.. |PySimpleGUI| image:: https://img.shields.io/pypi/dd/pysimplegui?color=orange&label=pysimplegui&style=plastic
   :target: https://pypi.org/project/PySimpleGUI/
   :alt: PyPI - PySimpleGUI
