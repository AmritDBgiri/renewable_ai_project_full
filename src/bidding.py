def conservative_bid(available, factor=0.1): return max(0, available*(1-factor))
def price_markup(base, vol): return base*(1+0.02+0.08*vol)