#!/bin/bash

for el in gros-40.nancy.grid5000.fr gros-41.nancy.grid5000.fr gros-42.nancy.grid5000.fr gros-43.nancy.grid5000.fr gros-44.nancy.grid5000.fr gros-45.nancy.grid5000.fr gros-46.nancy.grid5000.fr gros-47.nancy.grid5000.fr gros-48.nancy.grid5000.fr gros-49.nancy.grid5000.fr gros-5.nancy.grid5000.fr gros-50.nancy.grid5000.fr gros-51.nancy.grid5000.fr gros-52.nancy.grid5000.fr gros-53.nancy.grid5000.fr gros-54.nancy.grid5000.fr gros-55.nancy.grid5000.fr gros-56.nancy.grid5000.fr gros-57.nancy.grid5000.fr gros-58.nancy.grid5000.fr gros-59.nancy.grid5000.fr gros-6.nancy.grid5000.fr gros-60.nancy.grid5000.fr gros-61.nancy.grid5000.fr gros-62.nancy.grid5000.fr gros-63.nancy.grid5000.fr gros-64.nancy.grid5000.fr gros-65.nancy.grid5000.fr gros-66.nancy.grid5000.fr gros-67.nancy.grid5000.fr gros-68.nancy.grid5000.fr gros-69.nancy.grid5000.fr; do
        scp -i ~/.ssh/bench root@$el:/tmp/logs/* ./$el
done
