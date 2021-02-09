BOT_NAME = 'crelove'

SPIDER_MODULES = ['crelove.spiders']
NEWSPIDER_MODULE = 'crelove.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'crelove.pipelines.CrelovePipeline': 100,

}