import os
import pdfkit
import markdown


in_dir = 'site/en/tutorials'   # this will be relative_path"
toc_level = 3
in_dir = 'site/en/guide'   # this will be relative_path"
#in_dir = 'site/en/community'   # this will be relative_path"
#in_dir = 'site'
# in_dir = 'site/en/tutorials'   # this will be relative_path"
out_dir = os.path.join("html", in_dir)
out_html_path = os.path.join(out_dir, "index.html")
out_toc_path = os.path.join(out_dir, "toc.txt")
out_images_path = os.path.join(out_dir, "images")

cmd = "rm -rf {} ; mkdir -p {}".format(out_dir, out_images_path)
os.system(cmd)

cmd = "echo '' >  {}".format(out_html_path)
os.system(cmd)

oo_toc = open(out_toc_path, 'w')

files_txt = []
for root, subFolders, files in os.walk(in_dir):
    # copy image to prevent relative path miss
    toc_depth = len(root.split('/'))-4
    if 'images' in subFolders:
        path = os.path.join(root, 'images')
        m_files1 = os.listdir(out_images_path)
        m_files2 = os.listdir(path)
        if set(m_files1) & set(m_files2):
            print 'BADLLY IMGES', m_files1, m_files2
        # better to recursive merge
        cmd = "cp -rf {}/* {}".format(path, out_images_path)
        os.system(cmd)

    nb_file_paths = [os.path.join(root,filename) for filename in files if filename.endswith('.ipynb')]
    md_file_paths = [os.path.join(root,filename) for filename in files if filename.endswith('.md')]
    if toc_depth>=0 and (nb_file_paths or md_file_paths or 'images' not in root):
        oo_toc.write(toc_depth*4*' '+root.split('/')[-1]+'\n')
    print "md_files = " , md_file_paths
    for file_path in md_file_paths:
        out_path = file_path[:-3]+'.html'
        markdown.markdownFromFile(
            input=file_path,
            output=out_path,
            encoding='utf8'
        )
        cmd = "cat {} >> {}".format(out_path, out_html_path)
        os.system(cmd)
        oo_toc.write((toc_depth+1)*4*' '+file_path[:-3].split('/')[-1]+'\n')

    print "nb_files = " , nb_file_paths
    if nb_file_paths:
        ss = ''
        for f in nb_file_paths:
            ss = ss + ' "' + f + '"'
            oo_toc.write((toc_depth+1)*4*' '+f[:-6].split('/')[-1]+'\n')

        cmd = 'jupyter nbconvert ' + ss + ' --to html --stdout >> {}'.format(out_html_path)
        os.system(cmd)
