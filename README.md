# Insider Threat

* Insider Threat Program Documentation
* The default artifact saves automatically as <_build/pdf/insiderthreat.pdf>

## Browsing docs

* **Locally**  Browse to <_build/index.html> for a local view.
* **Remotely** Drop the contents of <_build/html> into a docroot.
* **As a PDF** Open it in your browser or favorite PDF reader.

## Building docs

* Install prerequisites, including Pip3, Git, and Rst2pdf.
* Clone this repository.
* Make the pdf, which also cleans the build and makes the HTML pages.

```
pip3 install --user sphinx_rtd_theme || echo "Could not install theme.  Will use default."
git clone https://github.com/dimitry-dukhovny/insiderthreat.git
cd insiderthreat
make pdf
```
