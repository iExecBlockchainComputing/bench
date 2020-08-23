# Bench list TODO

- 122 noeuds: 
    - **ID=1** Normal a charge basse **Scenario 3** 60 Txs during 300
    - **ID=2** Normal a charge haute **Scenario 4** 180 Txs during 300
- 62 noeuds:
    - **ID=3** Normal a charge basse **Scenario 2** 60 Txs during 300
    - **ID=4** Normal a charge haute 
- 32 noeuds:
    - **ID=5** Normal a charge basse **Scenario 1** 60 Txs during 300
    - **ID=6** Normal a charge haute **Scenario 5** 180 Txs during 300
    - **ID=7** (10) charge basse  -> (60) kill 16 (200) -> charge basse (610)
    - **ID=8** (10) charge basse  -> (11) latency 100ms (110) -> (111) latency 200ms (210) -> (211) latency 300ms (310) -> (311) latency 400ms (410) -> (411) latency 500ms (510) -> charge basse (610)
    - **ID=9** (10) charge basse -> (11) debit 1Mb (110) -> (111) debit 500Kbs (210) -> (211) debit 250Kbs (310) -> (311) debit 128Kbs (410) -> (411) debit 64Kbs (510) -> charge basse (610)
    - **ID=10** charge 319Tx + block step 3sec
    - **ID=11** block size 10x + block step 3sec
    - **ID=12** (10) charge basse -> (11) debit 40Mb (110) -> (111) debit 20Mb (210) -> (211) debit 10Mb (310) -> (311) debit 5mb (410) -> (411) debit 2.5Mb (510) -> charge basse (610)
