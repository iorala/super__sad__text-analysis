{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class DataVisualiser:\n",
    "    # ...\n",
    "\n",
    "    def save_visualizations(self, file_prefix):\n",
    "        bar_chart_file = file_prefix + \"_bar_chart.png\"\n",
    "        pie_chart_file = file_prefix + \"_pie_chart.png\"\n",
    "\n",
    "        # Bar Chart speichern\n",
    "        bar_chart = self.plot_bar_chart()\n",
    "        bar_chart.write_image(bar_chart_file)\n",
    "\n",
    "        # Pie Chart speichern\n",
    "        pie_chart = self.plot_pie_chart()\n",
    "        pie_chart.write_image(pie_chart_file)\n",
    "\n",
    "        return bar_chart_file, pie_chart_file\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [
    "sentiments_dict = {\"Positiv\": 2, \"Negativ\": 1, \"Neutral\": 3}\n",
    "visualizer = DataVisualiser(sentiments_dict)\n",
    "\n",
    "# Diagramme erstellen\n",
    "fig_1 = visualizer.plot_bar_chart()\n",
    "fig = visualizer.plot_pie_chart()\n",
    "\n",
    "# Diagramme speichern\n",
    "bar_chart_file, pie_chart_file = visualizer.save_visualizations(\"sentiment_analysis\")\n",
    "\n",
    "print(\"Bar Chart wurde gespeichert unter:\", bar_chart_file)\n",
    "print(\"Pie Chart wurde gespeichert unter:\", pie_chart_file)"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "is_executing": true
    }
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
