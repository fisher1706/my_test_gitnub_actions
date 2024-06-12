balances = """
{
    balances(date: "%s", page: %s, first: %s) {
        data {
            qty
            r1
            changed_at
            warehouse {
                code
                source
            }
            product {
                sku
            }
        }
        paginatorInfo {
            currentPage
            lastPage
            lastDate
            uuid
        }
    }
}
"""


productItems = """
{
    productItems(date: "%s", page: %s, first: %s) {
        data {
            erp_id
            attribute_set_id
            sku
            erp_completed
            erp_blocked
            erp_name
            erp_group
            erp_article
            erp_project
            erp_manufacturer_id
            erp_competera_enable
            erp_competera_reprice_enable
            erp_product_cost
            erp_manufacturer_name
            erp_tm_id
            erp_tm_name
            erp_version
            erp_model_id
            erp_model_name
            erp_cm_id
            erp_cm_name
            erp_material_id
            erp_material_name
            erp_season_id
            erp_season_name
            erp_item_size
            erp_group_id
            erp_group_name
            erp_subgroup_id
            erp_subgroup_name
            erp_subgroup2_id
            erp_subgroup2_name
            erp_subgroup3_id
            erp_subgroup3_name
            erp_color_id
            erp_color_hex
            erp_color_name
            erp_age_id
            erp_age_name
            erp_age_start_month
            erp_age_end_month
            erp_gender_id
            erp_gender_name
            erp_item_weight
            erp_item_bulk
            erp_clasp_id
            erp_clasp_name
            erp_tax_rate
            erp_web_status
            erp_web_threshold
            erp_new_date_end
            erp_spec_price_end
            erp_sales_xit
            erp_prom_ua
            erp_d_spec_price_begin
            erp_d_spec_price_end
            erp_vgc_width
            erp_vgc_lenght
            erp_vgc_height
            erp_barcode
            erp_supplier_id
            updated_at
            changed_at
        }
        paginatorInfo {
            currentPage
            lastPage
            lastDate
            uuid
        }
    }
}
"""


if __name__ == '__main__':
    data = "2024-04-30 13:41:04"
    page = "100"
    count = "5"

    x = balances % (data, page, count)
    print(x)
