#!/bin/bash

for el in gros-70.nancy.grid5000.fr gros-71.nancy.grid5000.fr gros-72.nancy.grid5000.fr gros-73.nancy.grid5000.fr gros-74.nancy.grid5000.fr gros-75.nancy.grid5000.fr gros-76.nancy.grid5000.fr gros-77.nancy.grid5000.fr gros-78.nancy.grid5000.fr gros-79.nancy.grid5000.fr gros-80.nancy.grid5000.fr gros-81.nancy.grid5000.fr gros-82.nancy.grid5000.fr gros-83.nancy.grid5000.fr gros-84.nancy.grid5000.fr gros-85.nancy.grid5000.fr gros-86.nancy.grid5000.fr gros-87.nancy.grid5000.fr gros-88.nancy.grid5000.fr gros-89.nancy.grid5000.fr gros-90.nancy.grid5000.fr gros-91.nancy.grid5000.fr gros-92.nancy.grid5000.fr gros-93.nancy.grid5000.fr gros-94.nancy.grid5000.fr gros-95.nancy.grid5000.fr gros-96.nancy.grid5000.fr gros-97.nancy.grid5000.fr gros-98.nancy.grid5000.fr gros-99.nancy.grid5000.fr gros-8.nancy.grid5000.fr gros-9.nancy.grid5000.fr; do
	scp -i ~/.ssh/bench root@$el:/tmp/logs/* ./$el
done

