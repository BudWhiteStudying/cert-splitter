### Python Certificate Splitter
Basic Python script that splits a `.pem` file containing multiple certificates into multiple `.pem` files containing one certificate each.

The script works by looking for `BEGIN CERTIFICATE` and `END CERTIFICATE` clauses within the collection file.

##### Test run
```
python src/cert-splitter.py test/google-roots.pem
```