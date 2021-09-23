<template>
    <LoggedinSidebarTemplate page_name="research">
        <template v-slot:main-content>
            <div class="max-w-xl mx-auto mb-10 sm:mb-0 min-h-screen">
                <div class="max-w-xl mx-auto lg:px-4">
                <div id="explanation" ref="explanation" class="relative w-full" tabindex="-1" style="top: -4.2rem;"></div>

                    <section id="core-data" class="sect">
                        <div class="flex items-center w-full mb-2">
                            <!-- eslint-disable-next-line max-len --><!-- prettier-ignore -->
                            <div class="sano-border-shine sano-border-shine-orange bg-white w-7 h-7 rounded mr-3 flex flex-col justify-center items-center">
                                <svg class="pl-px w-5 h-3 relative sano-svg-red-orange z-10">
                                    <use xlink:href="#sano-symbol" />
                                </svg>
                            </div>
                            <h2 class="text-sano-burgundy text-xl">
                                My Studies
                            </h2>
                        </div>
                        List the studies here...
                        <div class="study" v-for="study in studies">
                            <div class="name-section">
                                <div class="name">
                                    {{study.title}}
                                </div>
                                <div class="runby">
                                    Run by Placeholder
                                </div>
                            </div>
                            <div class="status-section">
                                <div class="enroll">
                                    ENROLLED
                                </div>
                                <div class="progress complete">
                                    COMPLETE
                                </div>
                            </div>
                            <div class="action-section">
                                <!-- TODO: use study.enrolled instead. -->
                                <button v-show='study.visible' class="join" @click="join(study)">
                                    Join study
                                </button>
                                <button v-show='!study.visible' class="leave" @click="leave(study)">
                                    Leave study
                                </button>
                            </div>
                        </div>
                    </section>
                </div>
                </div>
            </div>
        </template>
        <template v-slot:sidebar-content>
        </template>
    </LoggedinSidebarTemplate>
</template>

<script>

import LoggedinSidebarTemplate from "@/layouts/LoggedinSidebarTemplate";

export default {
    name: "Research",
    components: {
        LoggedinSidebarTemplate,
    },
    data() {
        return {
            studies: null,
        };
    },
    created() {
        this.$api.pub
            .get_studies()
            .then(response => {
                this.studies = response.data;
            });
    },
    methods: {
        join(study) {
            this.$api.user
                .join(study.key)
                .then(() => {
                    study.visible = false;
                })
                .catch(() => {
                    this.$toast({
                        type: "error",
                        title: "There was a problem joing the study.",
                    });
                });
        },
        leave(study) {
            this.$api.user
                .leave(study.key)
                .then(() => {
                    study.visible = true;
                })
                .catch(() => {
                    this.$toast({
                        type: "error",
                        title: "There was a problem leaving the study.",
                    });
                });
        },
    },
};
</script>

<style scoped lang="scss">
.mobile-sticky {
    top: 1rem;
}

.sect {
    @apply relative mt-6 mx-4 px-4 py-6 border border-sano-pink rounded overflow-hidden bg-white;
    @media (min-width: 992px) {
        @apply p-8 mx-0;
    }
}

@media (max-width: 575px) {
    .mobile-sticky {
        @apply sticky bg-white -ml-4 px-4 border-b border-sano-pink;
        z-index: 99;
        top: 0;
        width: calc(100% + 2rem);
    }

    .sano-toggle-label.sano-toggle-label {
        padding: 0 0.75rem;
    }
}

.study {
    border-color: #f7d2d2;
    border-style: solid;
    border-width: 1px;
    margin: 10px;
    padding: 10px;
}
.study .name-section {
    color: #54223b;
}
.study .name-section .name {
    font-size: 1.25rem;
}
.study .name-section .runby {
    color: #54223b;
}
.study .status-section {
    font-size: .9375rem;
}
.study .status-section .enroll {
    color: #F75338;
    font-size: .9375rem;
    margin-bottom: 5px;
}
.study .status-section .progress.complete {
    background-color: #3da498;
    border-radius: 9999px;
    color: white;
    text-align: center;
    width: 100px;
}
.study .action-section button {
    padding: 5px;
}
.study .action-section .join {
    background-color: #F75338;
    color: white;
}
.study .action-section .leave {
    background-color: #f7d2d2;
    color: #54223b;
}
@media (min-width: 992px) {
    .study .name-section {
        width: 50%;
    }
    .study .status-section {
        width: 25%;
    }
    .study .action-section {
        width: 25%;
    }
    .study .action-section button {
        width: 80%;
    }
    .study .name-section,
    .study .status-section,
    .study .action-section {
        display: inline-block;
    }
}
@media (max-width: 575px) {
    .study .status-section .enroll {
        float: left;
    }
    .study .status-section .progress.complete {
        float: right;
    }
    .study .action-section button {
        width: 100%;
    }
}
</style>
