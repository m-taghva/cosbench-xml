# cosbench-xml
scripts for generating xml configuration file in cosbench a bench marking tool for testing swift object storage.

      (customize-xml.py) this script can generate many xml configuration with uniq name and different config.
      use: # python3 customize-xml.py
      output: swift_config_sample_(n).xml
      ===========================================
      (s-xmlgen-n.py) in workload-gen directory just edit worker number in main work stage.
      you can send your maximum worker number to script and it can generate new xml file. it can count double from 2 until maximum-1. its make same number for every main.
      use: # python3 xmlgen.py <xml file path> <max number>
      ===========================================
      (d-xmlgen-n.py) in workload-gen directory just edit worker number in main work stage.
      you can send your maximum worker number to script and it can generate new xml file. it can count double from 2 until maximum. its make different number for every main. 
      use: # python3 xmlgen.py <xml file path> <max number>
      ===========================================
      wl-maker.py can run all scripts of workload directory. 
      save your directory and max number in wl-address.txt like it's orginal structure.
      use: # python3 wl-maker.py 
      ---> all output xml save in "all-xml" directory
