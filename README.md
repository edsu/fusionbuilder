This is an abomination. I inherited a WordPress blog with the [Fusion Page
Builder] plugin installed. When I wanted to use the WordPress XML export file
to move to a static site generator the post text was littered with lots of
Fusion tags and codes. I wanted to parse them out into a DOM like tree
structure and also strip them out. 

```python
import fusionbuilder
root, text = fusionbuilder.parse(text)
```

[Fusion Page Builder]: https://wordpress.org/plugins/fusion/
